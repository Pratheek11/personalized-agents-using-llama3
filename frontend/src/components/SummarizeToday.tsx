import { Button } from 'primereact/button'
import React, { useEffect } from 'react'
import styled from 'styled-components'
import {marked} from 'marked';

const SummarizeToday = () => {
  const [todaySummary, setTodaySummary] = React.useState<string>('');
  const [loading, setLoading] = React.useState<boolean>(false);

  const fetchSummary = async () => {
    try {
      setLoading(true);
      setTodaySummary(''); // Clear previous content
      
      const response = await fetch('http://localhost:8000/mcp/prompt', {
        body: JSON.stringify({
          query: 'Summarize today events',
        }),
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
      });

      if (!response.ok) {
        throw new Error('Network response was not ok');
      }

      // Get the reader from the response body
      const reader = response.body?.getReader();
      if (!reader) {
        throw new Error('No reader available');
      }

      const decoder = new TextDecoder();
      let buffer = '';

      while (true) {
        const { done, value } = await reader.read();
        
        if (done) {
          break;
        }

        // Decode the chunk
        buffer += decoder.decode(value, { stream: true });
        
        // Process complete lines
        const lines = buffer.split('\n');
        buffer = lines.pop() || ''; // Keep incomplete line in buffer
        
        for (const line of lines) {
          if (line.startsWith('data: ')) {
            try {
              const data = JSON.parse(line.slice(6)); // Remove 'data: ' prefix
              
              if (data.type === 'token') {
                // Append each token to the summary
                setTodaySummary(prev => prev + data.content);
              } else if (data.type === 'final_response') {
                // Set the final response (if your backend sends this)
                setTodaySummary(data.content);
              } else if (data.type === 'error') {
                setTodaySummary('Error: ' + data.content);
                break;
              } else if (data.type === 'done') {
                break;
              }
            } catch (parseError) {
              console.error('Failed to parse SSE data:', parseError);
            }
          }
        }
      }
      
      setLoading(false);
    } catch (error) {
      console.error('Fetch error:', error);
      setTodaySummary('Failed to fetch summary. Please try again later.');
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchSummary();
  }, []);

  return (
    <Container>
      <Header>
        <div></div>
        <div>
          {loading && (
            <i className="pi pi-spin pi-spinner" style={{ fontSize: '2rem' }}></i>
          )}
        </div>
        <Button 
          onClick={() => fetchSummary()} 
          disabled={loading} 
          label='Refresh' 
          icon="pi pi-refresh" 
          size='small'
        />
      </Header>
      <Body>
        <Code dangerouslySetInnerHTML={{ __html: marked(todaySummary) }}/>
      </Body>
    </Container>
  )
}

export default SummarizeToday

const Container = styled.div`
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
`

const Header = styled.div`
  width: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px;
`

const Body = styled.div`
  width: 100%;
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 10px;
  overflow: auto;
`

const Code = styled.pre`
  width: 100%;
  flex: 1;
  background-color:rgb(64, 64, 64);
  border-radius: 5px;
  text-wrap: wrap;
  overflow-y: auto;
  padding: 10px;
  margin: 0;
`
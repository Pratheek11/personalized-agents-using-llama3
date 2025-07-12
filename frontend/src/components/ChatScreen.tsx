import React from 'react'
import styled from 'styled-components'
import { Button } from 'primereact/button'

const ChatScreen = () => {
  const [disabled, setDisabled] = React.useState(false);
  return (
    <Container>
      <div>{/* Chat area */}</div>

      <MessageBox>
        <StyledTextarea disabled={disabled} placeholder="Ask anything..." />
        <div>
          <Button disabled={disabled} text rounded icon="pi pi-send" size="small" />
        </div>
      </MessageBox>
    </Container>
  )
}

export default ChatScreen

const Container = styled.div`
  width: 100%;
  height: 100%;
  padding-bottom: 100px; /* reserve space for fixed box */
  position: relative;
`

const MessageBox = styled.div`
  position: absolute;
  bottom: 10px;
  left: 10px;
  right: 10px;
  margin: 0 auto;
  background: #2c2c2c;
  border-radius: 8px;
  padding: 10px;
  display: flex;
  gap: 10px;
  align-items: center;
  color: #fff;
  z-index: 10;
`

const StyledTextarea = styled.textarea`
  flex: 1;
  resize: none;
  min-height: 40px;
  max-height: 120px;
  padding: 10px;
  border: none;
  background: transparent;
  color: #fff;
  outline: none;
  box-shadow: none;
  font-family: inherit;
  overflow-y: auto;

  &::placeholder {
    color: #aaa;
  }
`

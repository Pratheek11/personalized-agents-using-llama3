import React from 'react'
import Menubar from './Menubar'
import { TabView, TabPanel } from 'primereact/tabview';
import styled from 'styled-components';
import SummarizeToday from './SummarizeToday';
import Chat from './Chat';
        

function Home() {

  return (
    <div style={{ height: '100%'}}>
        <Menubar />
        <TabWrapper>
            <TabView>
                <TabPanel header="Chat" rightIcon="pi pi-comment">
                    <Chat />
                </TabPanel>
                <TabPanel header="Summarize Today" rightIcon="pi pi-bolt">
                    <SummarizeToday />
                </TabPanel>
            </TabView>
        </TabWrapper>
    </div>
  )
}

export default Home

const TabWrapper = styled.div`
  height: calc(100% - 41px);
  min-height: 0;
  display: flex;
  flex-direction: column;

  .p-tabview {
    height: 100%;
    min-height: 0;
    width: 100%;
    display: flex;
    flex-direction: column;
  }
  .p-tabview .p-tabview-nav {
    border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  }
  .p-tabview-panels {
    flex: 1 1 auto;
    height: 100%;
    min-height: 0;
    width: 100%;
    display: flex;
    flex-direction: column;
  }
  .p-tabview-panel {
    flex: 1 1 auto;
    height: 100%;
    min-height: 0;
    width: 100%;
    display: flex;
    flex-direction: column;
    padding: 0;
  }
  .p-tabview, .p-tabview-panels, .p-tabview-nav {
    background: inherit !important;
    color: inherit !important;
    padding: 0 !important;
  }
  .p-tabview-nav li .p-tabview-nav-link {
    color: inherit !important;
    background: inherit !important;
    gap: 0.2rem;
    font-size: 12px;
    border-color: rgba(0, 0, 0, 0);
  }
  .p-tabview .p-tabview-nav li.p-highlight .p-tabview-nav-link {
    background: #ffffff;
    border-color: #3b82f6;
    color: #3b82f6;
  }
`;
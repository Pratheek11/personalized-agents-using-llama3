import React, { useState } from 'react'
import styled from 'styled-components'
import ChatScreen from './ChatScreen'

const Chat = () => {
  const [collapsed, setCollapsed] = useState(false)

  return (
    <Container>
      <Sidebar collapsed={collapsed}>
        <ToggleButton onClick={() => setCollapsed(c => !c)}>
          <i className='pi pi-bars' />
        </ToggleButton>
        <Nav>
          <NavItem>
            <i className='pi pi-pen-to-square' /> 
            <NavText collapsed={collapsed}>New Chat</NavText>
          </NavItem>
        </Nav>
          <Collapsable collapsed={collapsed}>
          <Nav>
            <p style={{padding: '12px'}}>Chats</p>
            <NavItem>
              <i className='pi pi-history' /> 
              <NavText collapsed={collapsed}>History</NavText>
            </NavItem>
          </Nav>
          </Collapsable>
      </Sidebar>
      <Main>
        <ChatScreen/>
      </Main>
    </Container>
  )
}

export default Chat

const Container = styled.div`
  display: flex;
  background: #212121;
  color: #fff;
  height: 100%;
`

const Sidebar = styled.div<{ collapsed: boolean }>`
  width: ${({ collapsed }) => (collapsed ? '70px' : '260px')};
  background: #171717;
  display: flex;
  flex-direction: column;
  padding: 24px 0;
  border-right: 1px solid #212121;
  align-items: flex-start;
  transition: all 0.3s ease;
`

const ToggleButton = styled.button`
  margin-left: 16px;
  width: 32px;
  height: 32px;
  border-radius: 50%;
  border: none;
  background: transparent;
  color: #fff;
  cursor: pointer;
  z-index: 1;
  font-size: 1.2rem;
  transition: background 0.2s;
  &:hover {
    background: #262626;
  }
`

const Nav = styled.div`
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 12px;
  padding: 0 16px;
  margin-top: 16px;
  font-size: 12px;
`

const NavItem = styled.div`
  display: flex;
  align-items: center;
  padding: 12px;
  width: 100%;
  border-radius: 8px;
  cursor: pointer;
  transition: background 0.2s;
  &:hover {
    background: #262626;
  }
`

const NavText = styled.span<{ collapsed: boolean }>`
  margin-left: 8px;
  overflow: hidden;
  white-space: nowrap;
  opacity: ${({ collapsed }) => (collapsed ? 0 : 1)};
  transition: opacity 0.3s ease;
`
const Collapsable = styled.div<{ collapsed: boolean }>`
  overflow: hidden;
  width: 100%;
  transition: opacity 0.3s ease;
  opacity: ${({ collapsed }) => (collapsed ? 0 : 1)};
`

const Main = styled.div`
  flex: 1;
  overflow-y: auto;
  height: 100%;
`
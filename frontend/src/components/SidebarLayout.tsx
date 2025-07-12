// SidebarLayout.tsx
import React from 'react'
import styled from 'styled-components'

const SidebarLayout = ({ children }: { children: React.ReactNode }) => (
  <Container>
    <Sidebar>
      <Nav>
        <NavItem>New Chat</NavItem>
        <NavItem>History</NavItem>
        {/* Add more items as needed */}
      </Nav>
    </Sidebar>
    <Main>{children}</Main>
  </Container>
)

export default SidebarLayout

const Container = styled.div`
  display: flex;
  height: 100vh;
  background: #212121;
  color: #fff;
`

const Sidebar = styled.div`
  width: 260px;
  background: #171717;
  display: flex;
  flex-direction: column;
  padding: 24px 0;
  border-right: 1px solid #333;
`

const Logo = styled.div`
  font-size: 2rem;
  font-weight: bold;
  padding: 0 24px 24px 24px;
`

const Nav = styled.div`
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 12px;
  padding: 0 24px;
`

const NavItem = styled.div`
  padding: 12px;
  border-radius: 8px;
  cursor: pointer;
  transition: background 0.2s;
  &:hover {
    background: #262626;
  }
`

const Main = styled.div`
  flex: 1;
  padding: 32px;
  overflow-y: auto;
`
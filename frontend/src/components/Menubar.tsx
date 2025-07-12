import React from 'react'
import styled from 'styled-components'
import { Button } from 'primereact/button';
import { useNavigate } from 'react-router-dom';
        

const Menubar = () => {
  const navigate = useNavigate();
  return (
    <Container>
        {/* <Button label='PA' text link style={{color: 'black', fontSize: '24px'}}  onClick={() => navigate("/")} /> */}
        <h2 style={{color: 'white'}}>PA</h2>
        <Button icon="pi pi-user" rounded text severity='info' size='small' style={{ width: '32px', height: '32px', fontSize: '1rem', padding: 0, color: 'white' }} onClick={() => navigate('/profile')}/>
    </Container>
  )
}

export default Menubar

const Container = styled.div`
    height: 40px;
    padding: 20px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    border-bottom: 1px solid #212121;
`;
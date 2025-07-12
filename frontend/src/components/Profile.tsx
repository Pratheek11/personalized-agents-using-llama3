import { Button } from 'primereact/button'
import React from 'react'
import { useNavigate } from 'react-router-dom'

function Profile() {
    const navigate = useNavigate();
  return (
    <div>
        <div style={{padding: '20px', height: '40px', display: 'flex', alignItems: 'center', borderBottom: '1px solid #212121'}} >
            <Button text rounded  icon="pi pi-angle-left" className="p-button-outlined" style={{color: 'white'}} onClick={() => navigate('/')} />
        </div>
    </div>
  )
}

export default Profile
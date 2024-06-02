import { useState, useEffect } from 'react'
import './App.css'

function App() {
  const [users, setUsers] = useState([])

  useEffect(() => {
    fetchUsers()
  }, [])

  const fetchUsers = async () => {
    const response = await fetch('http://127.0.0.1:5000/users')
    const data = await response.json()

    setUsers(data.users)
    console.log(data.users)}



  return (
    <>

    </>
  )
}

export default App

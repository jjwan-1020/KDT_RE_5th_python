
import './styles/App.css'
import Header from './components/Header.jsx'
import { Route, Routes } from 'react-router-dom'
function App() {
  

  return (
    <div className="App">
      <Header />
      <Routes>
          <Route path='/' element={<h1>Home</h1>} />
          <Route path='/product' element={<h1>Products Page</h1>} />
          <Route path='/product/:productId' 
          element={<h1>Product Detail Page</h1>} />
      </Routes>
      
        
      </div>
  )
}

export default App

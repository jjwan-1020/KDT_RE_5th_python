
import './styles/App.css'
import Header from './components/Header.jsx'
import { Route, Routes } from 'react-router-dom'
import MainPage from './pages/MainPage.jsx'
import ProductPage from './pages/ProductPage.jsx'
import ProductDetailPage from './pages/ProductDetailPage.jsx'
import { useState, useEffect } from 'react';
import axios from 'axios';
function App() {
  const [products, setProducts] = useState([]);

  const getProducts = async () => {
    const res = await axios.get('https://jsonplaceholder.typicode.com/comments');
    console.log(res.data);
    setProducts(res.data.slice(0, 20));
  };

  useEffect(() => {
    getProducts();
  }, [])
  

  return (
    <div className="App">
      <Header />
      <Routes>
          <Route path='/' element={<MainPage />} />
          <Route path='/products' element={<ProductPage products={products}/>} />
          <Route path='/products/:productId' element={<ProductDetailPage products={products}/>} />
      </Routes>
      
        
      </div>
  )
}

export default App

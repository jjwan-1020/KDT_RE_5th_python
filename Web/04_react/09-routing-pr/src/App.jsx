import { Routes, Route } from 'react-router-dom'
import Navbar from './components/Navbar'
import Home from './pages/Home'
import Student from './pages/Student'
import SearchParams from './pages/SearchParams'
import NotFound from './pages/NotFound'

function App() {


  return (
    <>
      <div>
        <Navbar />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/student/:name" element={<Student />} />
          <Route path="/student.new" element={<SearchParams />} />
          <Route path="*" element={<NotFound />} />
        </Routes>
        
      </div>

    </>
  )
}

export default App

import { useSearchParams } from 'react-router-dom';
import '../styles/App.css';

function MainPage() {
  const [searchParams, setSearchParams] = useSearchParams();
  console.log(searchParams.get('mode')); // null or 'dark'

  return (
    <div className={`main ${searchParams.get('mode') === 'dark' ? 'dark' : ''}`}>
      <h1>Home</h1>

      <button onClick={() => setSearchParams({ mode: 'dark' })}>
        Dark Mode
      </button>
    </div>
  );
}

export default MainPage;

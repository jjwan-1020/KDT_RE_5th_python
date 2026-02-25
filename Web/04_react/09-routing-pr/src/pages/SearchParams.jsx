import { useSearchParams } from "react-router-dom";

function SearchParams() {
    const [searchParams] = useSearchParams();
    const name = searchParams.get('name');

    return (
        <div>
            <h1>SearchParams 페이지</h1>
            <p>이름: {name}</p>
        </div>
    );
}

export default SearchParams;
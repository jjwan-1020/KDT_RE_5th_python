import { useParams } from "react-router-dom";

function Student() {
    const { name } = useParams();

    return (
        <div>
            <h1>Student 페이지</h1>
            <p>학생 이름: {name}</p>
        </div>
    );
}

export default Student;
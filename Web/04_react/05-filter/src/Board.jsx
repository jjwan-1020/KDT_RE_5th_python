import { useState } from "react";

function Board() {
    const [writer, setWriter] = useState("");
    const [title, setTitle] = useState("");
    const [posts, setPosts] = useState([]);
    const [searchType, setSearchType] = useState("writer");
    const [keyword, setKeyword] = useState("");
    const addPost = () => {
        if (writer === "" || title === "") return;
        setPosts([
            ...posts,
            {
                id: posts.length + 1,
                writer,
                title,
            },
        ]),
        setWriter("");
        setTitle("");
    };
const filteredPosts = posts.filter((post) =>
    post[searchType].includes(keyword)
);
return (
    <div>
        작성자 :
        <input value={writer} onChange={(e) => setWriter(e.target.value)} />
        제목 :
        <input value={title} onChange={(e) => setTitle(e.target.value)} />
        <button onClick={addPost}>작성</button>
    <hr />
    <select onChange={(e) => setSearchType(e.target.value)}>
        <option value="writer">작성자</option>
        <option value="title">제목</option>
    </select>
    <input
    placeholder="검색어"
    value={keyword}
    onChange={(e) => setKeyword(e.target.value)}
    />
    <button>검색</button>
    <hr />
    <table border="1" width="100%">
        <thead>
            <tr>
                <th>번호</th>
                <th>제목</th>
                <th>작성자</th>
            </tr>
        </thead>
        <tbody>
            {filteredPosts.map((post) => (
                <tr key={post.id}>
                    <td>{post.id}</td>
                    <td>{post.title}</td>
                    <td>{post.writer}</td>
                </tr>
            ))}
        </tbody>
    </table>
</div>
);
}

export default Board;
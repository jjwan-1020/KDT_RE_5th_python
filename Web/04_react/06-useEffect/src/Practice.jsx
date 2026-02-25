import { useState, useEffect } from "react";
import Fake from "./Fake";

function Practice() {
    const [Posts, setPosts] = useState([]);
    useEffect(() => {
        setTimeout(() => {
            setPosts(Fake);
        }, 2000);
    }, []);

    return (
        <div>
            {Posts.length === 0 ? (
                <h2>로딩중</h2>
            ) : (
                <ul>
                    {Posts.map((post) => (
                        <li key={post.id}>
                            <h3>{post.title}</h3>
                            <p>{post.body}</p>
                            </li>
                    ))}
                </ul>
            )}
        </div>
    );
}

export default Practice;


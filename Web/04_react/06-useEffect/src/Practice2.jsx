import { useEffect, useState } from "react";

function Practice2() {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    const fetchPosts = async () => {
      try {
        const response = await fetch(
          "https://jsonplaceholder.typicode.com/posts"
        );
        const data = await response.json();
        setPosts(data);
      } catch (error) {
        console.error("데이터 불러오기 실패:", error);
      }
    };

    fetchPosts();
  }, []);

  return (
    <div>
      {posts.length === 0 ? (
        <h2>로딩중...</h2>
      ) : (
        posts.slice(0, 10).map((post) => (
          <div key={post.id}>
            <h3>{post.title}</h3>
            <p>{post.body}</p>
            <hr />
          </div>
        ))
      )}
    </div>
  );
}

export default Practice2;

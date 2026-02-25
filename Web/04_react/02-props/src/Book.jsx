const Book = (props) => {
    const { title, author, price, type } = props;
    return (
        <div className="book-card">
            <h3 className="best">이번주 베스트셀러</h3>
            <img 
                src="https://contents.kyobobook.co.kr/sih/fit-in/458x0/pdt/9791158513351.jpg"
                alt="book"
                className="book-img"
                />
                
            <h2 className="book-title">{title}</h2>
            <p>저자: {author}</p>
            <p>판매가: {price}원</p>
            <p>구분: {type}</p>
        </div>
    );
};

export default Book;
const form = document.querySelector("form");
const userInput = document.querySelector("#userid");
const commentInput = document.querySelector("#comment");
const commentList = document.querySelector(".comment-list");

form.addEventListener("submit", (e) => {
    e.preventDefault();
    const userId = userInput.value;
    const comment = commentInput.value;
    if (userId === "" || comment === "") return;
    const li = document.createElement("li");
    li.textContent = `${userId} - ${comment}`;
    commentList.appendChild(li);
    userInput.value = "";
    commentInput.value = "";
});

/*
const form = document.querySelector('form');
const list = document.querySelector(.comment-list);

form.addEventListener("submit", function(e) {
e.preventDefault();

const userid = form.elements.userid;
const comment = form.elements.comment;

const newComment = document.createElement("li");
newComment.innerHTML = `<b>${userid.value}</b> - ${comment.value}`;
list.append(newComment);


userid.value = "";
comment.value = "";
})
*/
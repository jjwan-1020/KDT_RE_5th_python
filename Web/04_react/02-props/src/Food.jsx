import React from "react";

const Food = (props) => {
    const { food = "피자" } = props;

    return (
        <div>
            제가 좋아하는 음식은<span style={{ color : 'red'}}>{food}</span>입니다
        </div>
    )
}
export default Food;

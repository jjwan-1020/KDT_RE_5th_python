import styled from "styled-components";

const StyledContainer = styled.div`
  display: flex;
`;

const StyledBox = styled.div`
  width: 100px;
  height: 100px;
  background-color: aliceblue;
`;

function StyledComponent() {
  return (
    <StyledContainer>
      <StyledBox />
    </StyledContainer>
  );
}

export default StyledComponent;

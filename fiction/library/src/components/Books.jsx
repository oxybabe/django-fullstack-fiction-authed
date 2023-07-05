import React from "react";

const Button = ({ text, onClick }) => {
  return (
    <>
      <h1>Book</h1>
      <button onClick={onClick}>{text}</button>
    </>
  );
};
export default Button;

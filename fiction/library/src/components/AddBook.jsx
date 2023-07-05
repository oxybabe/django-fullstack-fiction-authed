import React, { useState } from "react";

export default function AddBook({ handleAddBook }) {
  const [bookData, setBookData] = useState({
    title: "",
    author: "",
    description: "",
  });
  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setBookData((prevState) => ({
      ...prevState,
      [name]: value,
    }));
    //creates a new object by spreading the properties of prevState and then adding the [name] property with the value obtained from the input field
  };
  const handleFormSubmit = (e) => {
    e.preventDefault();
    handleAddBook(bookData);
    setBookData({
      title: "",
      author: "",
      description: "",
    });
    // resets the form after submitting
  };
  return (
    <>
      <div>AddBook</div>
      <form onSubmit={handleFormSubmit}>
        Book Title{" "}
        <input
          type="text"
          name="title"
          value={bookData.title}
          onChange={handleInputChange}
        />
        Author{" "}
        <input
          type="text"
          name="author"
          value={bookData.author}
          onChange={handleInputChange}
        />
        Description{" "}
        <input
          type="text"
          name="description"
          value={bookData.description}
          onChange={handleInputChange}
        />
        <button type="submit">Add Book</button>
      </form>
    </>
  );
}

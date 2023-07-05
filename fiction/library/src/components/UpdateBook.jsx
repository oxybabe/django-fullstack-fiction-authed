import { useState } from "react";
import React from "react";

export default function UpdateBook({ book, handleUpdateBook, setIsEditing }) {
  const [bookData, setBookData] = useState(book);
  const editFormSubmit = (e) => {
    e.preventDefault();
    handleUpdateBook(book.id, bookData);
    setBookData({
      id: "",
      title: "",
      author: "",
      description: "",
    });
    // resets the form after submitting
  };
  return (
    <>
      <div>Edit Book</div>
      <form onSubmit={editFormSubmit}>
        Book Title{" "}
        <input
          type="text"
          name="title"
          value={bookData.title}
          onChange={(e) => setBookData({ ...bookData, title: e.target.value })}
        />
        Description{" "}
        <input
          type="text"
          name="description"
          value={bookData.description}
          onChange={(e) =>
            setBookData({ ...bookData, description: e.target.value })
          }
        />
        <button type="submit">Submit Change</button>
      </form>
      <button
        onClick={() => {
          console.log("here");
          setIsEditing(false);
        }}
      >
        Cancel
      </button>
    </>
  );
}

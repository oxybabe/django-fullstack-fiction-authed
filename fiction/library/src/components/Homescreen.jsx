import React, { useEffect, useState } from "react";
import AddBook from "./AddBook";
import UpdateBook from "./UpdateBook";

const Homescreen = () => {
  const [data, setData] = useState([]);
  const [isAddBookFormShowing, setIsAddBookFormShowing] = useState(false);
  const [isEditing, setIsEditing] = useState(false);
  const [editedBook, setEditedBook] = useState({ ...data });

  async function addBook(bookData) {
    const response = await fetch("http://localhost:8000/books/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(bookData),
    });
    if (response.ok) {
      const result = await response.json();
      console.log("Success:", result);
      fetchData();
      setIsAddBookFormShowing(false);
    } else {
      console.error("Error:", error);
    }
  }
  //https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch#uploading_json_data
  async function fetchData() {
    try {
      const response = await fetch("http://127.0.0.1:8000/books/");
      const data = await response.json();
      setData(data);
    } catch (error) {
      console.error(error);
    }
  }
  useEffect(() => {
    fetchData();
  }, []);

  const deleteBook = async (id) => {
    try {
      const response = await fetch(`http://127.0.0.1:8000/books/${id}/`, {
        method: "DELETE",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ id }),
      });

      if (response.ok) {
        console.log("Book deleted!");
        fetchData();
      } else {
        console.log("Failed to delete book");
      }
    } catch (error) {
      console.log("An error occurred while deleting the book:", error);
    }
  };

  const handleUpdateBook = async (id, bookData) => {
    try {
      const response = await fetch(
        `http://127.0.0.1:8000/books/update/${id}/`,
        {
          method: "PATCH",
          headers: {
            "Content-Type": "application/json",
            // "X-CSRFToken": csrftoken,
          },
          body: JSON.stringify(bookData),
        }
      );

      if (response.ok) {
        console.log("Book updated!");
        fetchData();
      } else {
        console.log("Failed to update book");
      }
    } catch (error) {
      console.log("An error occurred while updating book:", error);
    }
  };

  return (
    <div>
      {data.map((book) => (
        <div
          style={{
            border: "2px solid white",
          }}
          key={book.id}
        >
          <div>Title: {book.title}</div>
          <div>Description: {book.description}</div>
          <button onClick={() => deleteBook(book.id)}>Delete Book</button>

          {isEditing ? (
            <UpdateBook
              book={book}
              handleUpdateBook={handleUpdateBook}
              setIsEditing={setIsEditing}
            />
          ) : (
            <button onClick={() => setIsEditing(true)}>Edit Book</button>
          )}
        </div>
      ))}
      {isAddBookFormShowing ? (
        <AddBook handleAddBook={addBook} />
      ) : (
        <button onClick={() => setIsAddBookFormShowing(true)}>Add Book</button>
      )}
    </div>
  );
};

export default Homescreen;

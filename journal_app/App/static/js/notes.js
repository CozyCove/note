document.addEventListener("DOMContentLoaded", () => {
  console.log("HELLO WORLD");
  async function getNotes() {
    try {
      const response = await fetch("/notes");
      if (!response.ok) {
        throw new Error(`HTTP ERROR! status: ${response.status}`);
      }
      const data = await response.json();

      return data;
    } catch (error) {
      console.error("Failed to fetch data:", error);
    }
  }
  function display(data) {
    const notes = document.getElementById("notes");
    const newNote = document.createElement("p");
    newNote.innerText = `data:${data.notes}`;
  }

  getNotes().then((data) => {
    const notes = document.getElementById("notes");
    data.notes.forEach((element) => {
      const newNote = document.createElement("p");
      newNote.innerText = `${element.text}`;
      notes.appendChild(newNote);
      console.log(data);
    });
  });
});

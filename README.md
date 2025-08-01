# Mongo Playground

**Mongo Playground** is a command-line tool that lets you write & test native mongosh commands in a file & execute it.  
It auto-reloads the file after each input, so you can experiment with MongoDB queries quickly — no repetitive typing, no copy-pasting, no history scrolling.

Perfect for students, instructors & developers who work with MongoDB & want a persistent, testable query environment.

---

## 🎯 Key Features

- ✍️ Write native mongosh commands (like use, show collections, db.collection.find() etc.)
- 🔄 Automatically reloads the file after any keypress
- 🖥️ Keeps output clean with optional terminal clearing
- 🔃 Reusable scripts for assignments, learning, demos
- 🔐 Uses environment variables to manage DB connection safely

---

## 🚀 How to Use

### 🛠️ 1. Install Mongo Playground

1. Download the `.msi` installer from the [Releases](#) section of this repository.  
2. Run the installer — it will:
   - Install Mongo Playground
   - Add its path to your system environment variables (so you can run it from anywhere using the `mp` command)

> ✅ **Note:** Make sure MongoDB Shell (mongosh) is installed & available in your system's PATH.

---

### 🔐 2. Setup Environment Variables

A `.env` file is already included; **please replace the values below with your own MongoDB connection info**:

```env
CLUSTER_LINK=mongodb+srv://user:pass@cluster.mongodb.net
DB_NAME=Practice # Optional
```
---

### 📂 3. Prepare Your Query File

Create a file (e.g. `query`) & write native mongosh commands in it:

```js
// switch database;
use myDatabase;

// create a collection;
db.createCollection("users");

// insert a document;
db.users.insertOne({ name: "Alice", age: 30 });

// find users;
db.users.find();
```
> ⚠️ **Important:** Add a semicolon (;) after every query — including after comments.  
> If a comment line does not end with a semicolon, the next query will be ignored or treated as part of the comment.

---

### ▶️ 4. Run the Tool

Open a terminal & run:

```cmd
mp --file path\to\query
```
---

### ⚙️ 5. Optional Flags

You can use these command-line flags:

| Flag            | Description                                                                 |
|-----------------|-----------------------------------------------------------------------------|
| --file          | **(Required)** Path to your MongoDB script file                             |
| --clusterlink   | MongoDB cluster connection string (default: reads from .env)                |
| --dbname        | MongoDB database name (default: reads from .env)                            |
| --clear         | Clears the terminal screen after each run (for cleaner output)              |

#### Example:

```cmd
mp --file Practice\query --clear
```
---

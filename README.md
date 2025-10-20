# AI-ML-Foundation


## Managing Multiple Project Folders in a Single Git Repository (One Branch per Folder using Worktrees)

This repository contains multiple independent project folders.
Each folder is tied to its **own Git branch**, using [Git Worktrees](https://git-scm.com/docs/git-worktree). This keeps the remote branches clean while letting you organize your local machine with separate folders.

### 📁 Structure Example

```
AI-ML/                    ← Main repo
│
├─ Python-For-ML/         ← Local folder for 'python-for-ml' branch
├─ Data-Engineering/      ← Local folder for 'data-engineering' branch
└─ README.md              ← Lives only in the main branch
```

On GitHub:

* The `python-for-ml` branch only contains the contents of `Python-For-ML/`
* The `data-engineering` branch only contains the contents of `Data-Engineering/`
* The `main` branch does **not** contain these folders (they're in `.gitignore` locally)

---

### 🧭 Why Worktrees?

Normally, you’d have to **checkout different branches in the same folder** to work on multiple projects — messy and slow.
Worktrees let you check out **multiple branches at once** into separate folders, while all staying in the same repo.

---

### 🛠 How to Add a New Project Folder

Suppose you want to add a new project called `Data-Engineering`:

1. **Create a new branch**

   ```bash
   git branch data-engineering
   ```

2. **Add a worktree** linked to that branch

   ```bash
   git worktree add "./Data-Engineering" data-engineering
   ```

3. **Go inside the new folder** and work as usual

   ```bash
   cd "Data-Engineering"
   # Add files, initialize code, etc.
   git add .
   git commit -m "Initialize Data Engineering project"
   git push origin data-engineering
   ```

4. **Ignore the folder on the main branch** so it doesn’t pollute main:
   Edit `.gitignore` on `main`:

   ```
   /Data-Engineering
   ```

   Then commit and push:

   ```bash
   git add .gitignore
   git commit -m "Ignore Data-Engineering folder in main"
   git push origin main
   ```

---

### 🌿 Adding More Worktrees

Repeat the above for every new project folder:

```bash
git branch new-project
git worktree add "./New-Project" new-project
```

---

### 📋 Useful Commands

List all worktrees:

```bash
git worktree list
```

Remove a worktree:

```bash
git worktree remove "./Data-Engineering"
```

Detach a branch but keep files:

```bash
git worktree remove --force "./Data-Engineering"
```

---

### 📝 Notes

* Each folder is **independent**. Commits inside one don’t affect the others.
* Push and pull inside each project folder as if it were its own repo.
* The root `README.md` stays in `main` and can document the overall structure.

---

This approach is ideal if you want **one repo** but **clean, isolated project branches**, without juggling multiple local clones.

---

Would you like me to add a short section explaining how to switch back to a worktree after restarting your computer (to avoid common path errors)?

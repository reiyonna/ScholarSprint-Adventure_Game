# ScholarSprint: Christ University Survival Adventure

In this unique 2D side-scrolling adventure built with `pygame`, you play as a determined student surviving the trials of Christ University, Lavasa campus life. It includes dodging security guards asking for your ID cards, collecting Cafe Chopsticks spring rolls, and taking CIA quizzes to progress through increasingly challenging levels.

---

## Game Overview

**Christ Survival** blends action-platformer mechanics with interactive mini-quizzes. You'll battle enemies, pick up items, shoot and throw grenades, while unlocking knowledge-based checkpoints to continue your journey.

### Game Features

* Campus locations and custom sprites
* Quiz popups to test your knowledge at key points
* Player and enemy animations: idle, run, jump, and death
* Grenades, bullets, and collectible item boxes
* Level data stored in `game.csv`
* Health bar and HUD with ammo and item pickups
* Explosions and screen fade transitions
* Spring Roll and ID Card collectible mechanics

---

## Project Structure

```plaintext
ScholarSprint-Adventure_Game/
│
├── assets/                # Additional media (gifs, images)
│
├── img/                   # All game sprites, backgrounds, UI buttons
│   ├── background/        # Scenery and environment
│   ├── enemy/             # Enemy animations
│   ├── player/            # Player animations
│   ├── tile/              # Terrain tiles
│   ├── explosion/         # Explosion sprite frames
│   └── icons/             # Icons like bullets, health, CIA, etc.
│
├── button.py              # Utility to create interactive buttons
├── popup.py               # Quiz interface and logic
├── game.py                # Main game logic and loop
├── christSurvival.py      # Alternate game script (legacy/testing)
├── game.csv               # Level layout and tile data
├── __pycache__/           # Python cache
```

---

## Requirements

* Python 3.7+
* `pygame` library

Install requirements:

```bash
pip install pygame
```

---

## 🚀 How to Run

In your terminal:

```bash
python game.py
```

If you want to try the alternate version (e.g., `christSurvival.py`):

```bash
python christSurvival.py
```

---

## Gameplay Mechanics

| Feature              | Keys / Controls                                   |
| -------------------- | ------------------------------------------------- |
| **Movement**         | ← → (Left/Right Arrow Keys), **Spacebar** to jump |
| **Shoot**            | **F** key (or **Left Ctrl** – commonly used)      |
| **Grenade**          | **G** key                                         |
| **Collectibles**     | Automatically collected on collision              |
| **Quiz Checkpoints** | Walk into **CIA icon** to trigger quiz            |
| **Death**            | Automatic on contact with water or 0 health       |
---

## The Quiz Mechanism

* Hitting a CIA (Continuous Internal Assessment as per Christ University) icon launches a quiz (`popup.py`)
* If you answer correctly, you’re allowed to continue
* Answering incorrectly may delay your progress!

---

## Level Design

* The level structure is grid-based and driven by `game.csv`.
* Each number in the CSV corresponds to a tile or object (e.g., player, enemy, health box, etc.)

---

Enjoy sprinting through your University survival! 

---
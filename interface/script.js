// Sample card data
const cards = [
  'fool', 'magician', 'high priestess', 'empress', 'emperor', 'hierophant', 'lovers', 
  'chariot', 'strength', 'hermit', 'wheel of fortune', 'justice', 'hanged-man', 'death',
  'temperance', 'devil', 'tower', 'star', 'moon', 'sun', 'judgement', 'world',
  'ace-of-cups', 'two-of-cups', 'three-of-cups', 'four-of-cups', 'five-of-cups',
  'six-of-cups', 'seven-of-cups', 'eight-of-cups', 'nine-of-cups', 'ten-of-cups',
  'page-of-cups', 'knight-of-cups', 'queen-of-cups', 'king-of-cups',
  'ace-of-pentacles', 'two-of-pentacles', 'three-of-pentacles', 'four-of-pentacles',
  'five-of-pentacles', 'six-of-pentacles', 'seven-of-pentacles', 'eight-of-pentacles',
  'nine-of-pentacles', 'ten-of-pentacles', 'page-of-pentacles', 'knight-of-pentacles',
  'queen-of-pentacles', 'king-of-pentacles',
  'ace-of-swords', 'two-of-swords', 'three-of-swords', 'four-of-swords', 'five-of-swords',
  'six-of-swords', 'seven-of-swords', 'eight-of-swords', 'nine-of-swords', 'ten-of-swords',
  'page-of-swords', 'knight-of-swords', 'queen-of-swords', 'king-of-swords',
  'ace-of-wands', 'two-of-wands', 'three-of-wands', 'four-of-wands', 'five-of-wands',
  'six-of-wands', 'seven-of-wands', 'eight-of-wands', 'nine-of-wands', 'ten-of-wands',
  'page-of-wands', 'knight-of-wands', 'queen-of-wands', 'king-of-wands'
];

// Function to shuffle the cards list
function shuffleCards() {
  for (let i = cards.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [cards[i], cards[j]] = [cards[j], cards[i]];
  }
}

// Function to generate card elements
function generateCards() {
  const container = document.getElementById("cardsContainer");
  shuffleCards();
  for (let i = 0; i < 78; i++) {
    const card = cards[i];
    const cardElement = document.createElement("div");
    cardElement.classList.add("card");
    cardElement.dataset.cardName = card;
    cardElement.innerHTML = `
      <img class="back" src="tarot_img/card_back.jpg">
      <img class="front" src="tarot_img/${card}.jpg">
      <img class="reversed-front" src="tarot_img/reversed_${card}.jpg">
    `;
    cardElement.addEventListener("click", () => toggleCard(cardElement));
    container.appendChild(cardElement);
  }
}

// Function to toggle card visibility and orientation
function toggleCard(cardElement) {
  cardElement.classList.toggle("flipped");
}

// Generate initial set of cards
generateCards();

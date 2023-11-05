import React from 'react';

interface CardProps {
  title: string;
  content: string;
}

const Card: React.FC<CardProps> = ({ title, content }) => (
  <div className="bg-gray-200 p-4 mb-4 max-width:100%">
    <div className="font-bold text-xl mb-2">{title}</div>
    <p className="text-gray-700 text-base">{content}</p>
  </div>
);

const CardGrid: React.FC = () => {
  const cardsData = [
    { title: 'Card 1', content: 'Lorem ipsum dolor sit amet' },
    { title: 'Card 2', content: 'Voluptatibus quia, nulla! Maiores et perferendis eaque.' },
    { title: 'Card 3', content: 'Exercitationem praesentium nihil.' },
    { title: 'Card 1', content: 'Lorem ipsum dolor sit amet' },
    { title: 'Card 2', content: 'Voluptatibus quia, nulla! Maiores et perferendis eaque.' },
    { title: 'Card 3', content: 'Exercitationem praesentium nihil.' },
    { title: 'Card 1', content: 'Lorem ipsum dolor sit amet' },
    { title: 'Card 2', content: 'Voluptatibus quia, nulla! Maiores et perferendis eaque.' },
    { title: 'Card 3', content: 'Exercitationem praesentium nihil.' },
    
    // Add more card data objects here as needed
  ];

  return (
    <div className="grid grid-cols-3 gap-4 mx-5">
      {cardsData.map((card, index) => (
        <Card key={index} title={card.title} content={card.content} />
      ))}
    </div>
  );
}

export default CardGrid;

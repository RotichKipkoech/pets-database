import React from 'react';
import Header from './Header';
import Footer from './Footer';
import ServicesSection from './ServicesSection';
import Projects from './Projects';

const Home = () => {

  const coverPageStyle = {
    backgroundImage: `url('/ii.jpg')`
  };

  // Sample review data
  const reviews = [
    {
      name: 'John Maingi',
      rating: 5,
      reviewText: 'Excellent service! They fixed my plumbing issues quickly and professionally.',
    },
    {
      name: 'Michael Ndegwa',
      rating: 4,
      reviewText: "M.Solution Plumbing provided great service. I'm satisfied with their work.",
    },
    {
      name: 'Alex Johnson',
      rating: 5,
      reviewText: 'I highly recommend M.Solution Plumbing. They are reliable and efficient.',
    },
  ];

  return (
    <>
      <Header />
      <div className="cover-page" style={coverPageStyle}>
        {/* <h2>Welcome to M.Solution Plumbing</h2> */}
        <div className="slide">
          <div className="content">
            <h2>M.SOLUTION PLUMBING</h2>
            <h3>Best Plumbing and maintenance service providers in Kenya</h3>
            <div className="buttons">
              <button id="bt1">Contact Us</button>
              <button id="bt2" onClick={<ServicesSection/>}>Our Services</button>
            </div>
          </div>
        </div>
        </div>

        <div className="home">


        <div className="main">
      <div className="image">
        <img src="./basin1.jpeg" alt="image" />
        <h2>Washroom Toilet & Sink Installation</h2>
        <p>we offer sanitary appliances  repairs and installations. We also install and repair kitchen sinks and washhand basins . We make sure that all our work is done to the highest standards of safety and efficiency.</p>
      </div>

      {/* Repeat the following block for each service */}
      <div className="image">
        <img src="/toilet.jpeg" alt="image" />
        <h2>Washroom Toilet Repair & Installation</h2>
        <p>we offer water closset repairs and installations. We make sure that all our work is done to the highest standards of safety and efficiency.</p>
      </div>

      
      <div className="image">
        <img src="./toile2.jpeg" alt="image"/>
        <h2>Washroom  Basin Repair & Installation</h2>
        <p> we offer Grab rail for the elderly and disabbled at an affordable cost.We also install arabic showers and telephonic showers . 
             We make sure that all our work is done to the highest standards of safety and efficiency.</p>
      </div>
      </div>

        {/* Review section */}
        <h2>Customer Reviews</h2>
        <div className="reviews">
          <div className="review">
            <div className="review-info">
              <h3>{reviews[0].name}</h3>
              <div className="rating">
                {Array.from({ length: reviews[0].rating }, (_, index) => (
                  <span key={index} className="star">&#9733;</span>
                ))}
              </div>
            </div>
            <p>{reviews[0].reviewText}</p>
          </div>
          <div className="review">
            <div className="review-info">
              <h3>{reviews[1].name}</h3>
              <div className="rating">
                {Array.from({ length: reviews[1].rating }, (_, index) => (
                  <span key={index} className="star">&#9733;</span>
                ))}
              </div>
            </div>
            <p>{reviews[1].reviewText}</p>
          </div>
          <div className="review">
            <div className="review-info">
              <h3>{reviews[2].name}</h3>
              <div className="rating">
                {Array.from({ length: reviews[2].rating }, (_, index) => (
                  <span key={index} className="star">&#9733;</span>
                ))}
              </div>
            </div>
            <p>{reviews[2].reviewText}</p>
          </div>
        </div>
      </div>
      <Footer />
    </>
  );
};

export default Home;

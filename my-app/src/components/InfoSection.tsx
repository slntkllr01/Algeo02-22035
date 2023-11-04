import React from 'react';

function InfoSection({ numResults, executionTime }) {
    return (
      <div className="flex justify-between p-4">
        <p>
          <span className="font-bold">{`<${numResults}>`} Results</span> in{' '}
          <span className="font-bold">{`<${executionTime}>`} seconds</span>
        </p>
      </div>
    );
  }
  
  export default InfoSection;
// components/PatientForm.js
import React, { useState } from 'react';

const PatientForm = ({ onNewPatient }) => {
  const [newPatient, setNewPatient] = useState({
    name: '',
    age: '',
    gender: '',
    contactNumber: '',
    address: '',
  });

  const handleChange = (field, value) => {
    setNewPatient((prevPatient) => ({ ...prevPatient, [field]: value }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    // Assuming you have a submitPatient function in your api.js
    submitPatient(newPatient)
      .then((submittedPatient) => {
        // Clear the form and update the list of patients with the new one
        setNewPatient({
          name: '',
          age: '',
          gender: '',
          contactNumber: '',
          address: '',
        });
        onNewPatient(submittedPatient);
      })
      .catch((error) => console.error('Error submitting patient:', error));
  };

  return (
    <form onSubmit={handleSubmit}>
      <h3>Add New Patient</h3>
      <label>Name:</label>
      <input
        type="text"
        value={newPatient.name}
        onChange={(e) => handleChange('name', e.target.value)}
      />
      <label>Age:</label>
      <input
        type="text"
        value={newPatient.age}
        onChange={(e) => handleChange('age', e.target.value)}
      />
      <label>Gender:</label>
      <input
        type="text"
        value={newPatient.gender}
        onChange={(e) => handleChange('gender', e.target.value)}
      />
      <label>Contact Number:</label>
      <input
        type="text"
        value={newPatient.contactNumber}
        onChange={(e) => handleChange('contactNumber', e.target.value)}
      />
      <label>Address:</label>
      <input
        type="text"
        value={newPatient.address}
        onChange={(e) => handleChange('address', e.target.value)}
      />
      <button type="submit">Submit</button>
    </form>
  );
};

export default PatientForm;

const diseases = {

  Dengue:{
    symptoms:[
      "high_fever",
      "joint_pain",
      "skin_rash",
      "severe_headache"
    ],

    solution:
      "IV Fluids, Hydration Therapy, and Paracetamol.",

    description:
      "Mosquito-borne viral disease causing fever and joint pain."
  },

  Malaria:{
    symptoms:[
      "high_fever",
      "chills",
      "sweating",
      "muscle_pain",
      "nausea"
    ],

    solution:
      "Artemisinin Combination Therapy and Anti-Malarial Drugs.",

    description:
      "Parasitic infection spread through mosquito bites."
  },

  "COVID-19":{
    symptoms:[
      "dry_cough",
      "loss_of_smell",
      "fatigue",
      "breathlessness"
    ],

    solution:
      "Oxygen Support and Antiviral Medication.",

    description:
      "Respiratory viral infection affecting lungs and immunity."
  },

  Typhoid:{
    symptoms:[
      "abdominal_pain",
      "weakness",
      "high_fever"
    ],

    solution:
      "Azithromycin, Ceftriaxone, and Proper Hydration.",

    description:
      "Bacterial infection spread by contaminated food and water."
  },

  Chikungunya:{
    symptoms:[
      "joint_pain",
      "skin_rash",
      "swollen_joints",
      "high_fever"
    ],

    solution:
      "Rest Therapy, Hydration, and Anti-Inflammatory Medicines.",

    description:
      "Mosquito-borne disease causing swollen joints and pain."
  }

};

function runDiagnosis(){

  const checked = document.querySelectorAll(
    'input[type="checkbox"]:checked'
  );

  let selectedSymptoms = [];

  checked.forEach(box=>{
    selectedSymptoms.push(box.value);
  });

  const results = document.getElementById("results");

  results.innerHTML = "";

  let diseaseFound = false;

  for(let disease in diseases){

    let matched = [];

    diseases[disease].symptoms.forEach(symptom=>{

      if(selectedSymptoms.includes(symptom)){
        matched.push(symptom);
      }

    });

    const probability = (
      matched.length /
      diseases[disease].symptoms.length
    ) * 100;
     if(matched.length >= 2){

      diseaseFound = true;

      results.innerHTML += `

        <div class="result-card">

          <h2>${disease}</h2>

          <p>
            <strong>Match Probability:</strong>
            ${probability.toFixed(1)}%
          </p>

          <p>
            <strong>Description:</strong>
            ${diseases[disease].description}
          </p>

          <p>
            <strong>Matched Symptoms:</strong>
            ${matched.join(', ')}
          </p>

          <p>
            <strong>Recommended Solution:</strong>
            ${diseases[disease].solution}
          </p>

        </div>

      `;
    }

  }

  if(!diseaseFound){

    results.innerHTML = `

      <div class="result-card">
        <h2>No Strong Match Found</h2>
        <p>Please select more symptoms for better diagnosis.</p>
      </div>

    `;
  }

}

function clearDiagnosis(){

  document.querySelectorAll(
    'input[type="checkbox"]'
  ).forEach(box=>{
    box.checked = false;
  });

  document.getElementById("patientName").value = "";

  document.getElementById("results").innerHTML = `

    <div class="empty-box">
      <h2>Select symptoms and click Run Diagnosis</h2>
    </div>

  `;
}

function scrollToDiagnosis(){

  document.getElementById("diagnosis")
  .scrollIntoView({
    behavior:"smooth"
  });

}
import pandas as pd
import streamlit as st

# Load job data from a CSV file
job_data = pd.read_csv('processed_data.csv')

# Define the app structure
st.title('Job Search App')

# Add an image
image = st.image('image.jpg', caption='Job Search')

# Add search bar and button
search_term = st.text_input('Search by job title or keyword:')
location = st.text_input('Location:')
search_button = st.button('Search')

# Filter job data based on search criteria when the button is clicked
if search_button:
    if search_term and location:
        filtered_data = job_data[
            (job_data['Job Title'].str.contains(search_term, case=False)) &
            (job_data['Location'].str.contains(location, case=False))
        ]
    elif search_term:
        filtered_data = job_data[
            job_data['Job Title'].str.contains(search_term, case=False)
        ]
    elif location:
        filtered_data = job_data[
            job_data['Location'].str.contains(location, case=False)
        ]
    else:
        filtered_data = None
else:
    filtered_data = None

# Display filtered job data or 'No jobs found' message
if filtered_data is not None and len(filtered_data) > 0:
    st.subheader(f'Found {len(filtered_data)} jobs')
    st.dataframe(filtered_data)
elif filtered_data is not None:
    st.write('No jobs found based on the search criteria.')

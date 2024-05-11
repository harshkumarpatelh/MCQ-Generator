import pandas as pd
import matplotlib.pyplot as plt

# Function to create PDF
def create_pdf(df, filename):
    # Create a figure and axis object
    fig, ax = plt.subplots(figsize=(10, 5))

    # Hide the axes
    ax.axis('off')

    # Create a table and add it to the axis
    table = ax.table(cellText=df.values, colLabels=df.columns, loc='center')

    # Save the figure as a PDF
    plt.savefig(filename)

# # Sample data
# data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
#         'Age': [28, 35, 45, 30],
#         'City': ['New York', 'Paris', 'London', 'Berlin']}
# df = pd.DataFrame(data)

# def PDF(subject, data):
#     if st.button('Download PDF'):
#         filename = subject + ".pdf"
#         create_pdf(data,filename)
#         st.success('PDF file has been downloaded!')


# Add a link to download the PDF directly
# st.markdown('[Download PDF](dataframe.pdf)', unsafe_allow_html=True)
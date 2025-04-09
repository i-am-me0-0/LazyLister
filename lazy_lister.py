import os

def list_subfolder_files(subfolder_name, output_filename="file_list.txt"):
    """
    Lists all files in the specified subfolder and writes them to a text file.
    
    Args:
        subfolder_name (str): Name of the subfolder to scan
        output_filename (str): Name of the output text file (defaults to "file_list.txt")
    """
    try:
        # Ensure we're using absolute paths
        current_dir = os.path.dirname(os.path.abspath(__file__))
        subfolder_path = os.path.join(current_dir, subfolder_name)
        
        # Verify the subfolder exists
        if not os.path.exists(subfolder_path):
            raise FileNotFoundError(f"The subfolder '{subfolder_name}' does not exist")
            
        # Create the output file
        with open(output_filename, 'w') as f:
            # List all files in the subfolder
            for filename in os.listdir(subfolder_path):
                if os.path.isfile(os.path.join(subfolder_path, filename)):
                    f.write(filename + '\n')
                    
        print(f"Successfully wrote file list to {output_filename}")
        
    except Exception as e:
        print(f"Error: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Replace 'my_subfolder' with your actual subfolder name
    list_subfolder_files('input')
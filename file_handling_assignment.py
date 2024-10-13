def main():
  """Main function to handle file creation, writing, reading, appending, and error handling."""

  try:
    with open("my_file.txt", "w") as file:
      file.write("This is the first line.\n")
      file.write("This line contains a number: 42\n")
      file.write("The final line for initial creation.\n")
      print("Successfully created 'my_file.txt' and wrote content.")

    with open("my_file.txt", "r") as file:
      content = file.read()
      print("\n--- File Contents ---")
      print(content)
      print("--- End of File Contents ---")

    with open("my_file.txt", "a") as file:
      file.write("This is the first appended line.\n")
      file.write("Appending another line with a float: 3.14\n")
      file.write("The final appended line.\n")
      print("\nSuccessfully appended content to 'my_file.txt'.")

  except FileNotFoundError:
    print("Error: File 'my_file.txt' not found.")
  except PermissionError:
    print("Error: Insufficient permissions to access or modify 'my_file.txt'.")
  finally:
    print("\nScript execution completed.")

if __name__ == "__main__":
  main()
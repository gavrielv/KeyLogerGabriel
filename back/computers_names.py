import json
import os


class ComputersNames:
    """Managing and accessing the database of tracked computers."""

    def __init__(self, computers_file_path):
        """Initialize the database with stored data, and receive the file path for the database."""
        self.computers_file_path = computers_file_path
        try:
            if os.path.exists(computers_file_path):
                with open(computers_file_path, 'r') as file:
                    self.computers = json.load(file)
            else:
                self.computers = {'names': {}, 'unknown': {}}
        except Exception as e:
            self.computers = {'Error': f'Error reading file: {str(e)}'}

    def get_name(self, mac: str) -> str | None:
        """Return the computer name if it exists in the database."""
        if mac in self.computers['names']:
            return self.computers['names'][mac]
        elif mac in self.computers['unknown']:
            return f"unknown{self.computers['unknown'][mac]}"
        return None

    def add(self, mac_address: str, name: str | None = None) -> dict:
        """Add a new computer to the database, returns whether saving to file was successful."""
        if mac_address in self.computers['names'] or mac_address in self.computers['unknown']:
            return {False: 'Already in data (use update to change)'}
        if name:
            self.computers['names'][mac_address] = name
        else:
            self.computers['unknown'][mac_address] = max(self.computers['unknown'].values(), default=0) + 1
        return self._save()

    def _save(self) -> dict:
        """Save the changes to the file, returns the save status."""
        try:
            with open(self.computers_file_path, 'w', encoding='utf-8') as file:
                file.write(json.dumps(self.computers, ensure_ascii=False))
                return {'Status': "Saving successfully"}
        except Exception as e:
            return {'Error': f'Error reading file: {str(e)}'}

    # The following methods are currently unused but were prepared for potential use by an admin:

    def update(self, mac_address: str, name: str) -> dict:
        """Update the name for an existing mac address."""
        if mac_address in self.computers['names']:
            self.computers['names'][mac_address] = name
            return self._save()
        elif mac_address in self.computers['unknown']:
            self.computers['unknown'][mac_address] = name
            return self._save()
        return {'Error': 'Not found'}

    def delete(self, mac_address: str) -> dict:
        """Delete a computer from the database, returns the delete status."""
        is_changed = False
        if mac_address in self.computers['names']:
            del self.computers['names'][mac_address]
            is_changed = True
        elif mac_address in self.computers['unknown']:
            del self.computers['unknown'][mac_address]
            is_changed = True
        if is_changed:
            return self._save()
        return {False: "Not found"}

from app import app, mongo

def populate_equipment():
    with app.app_context():
        # Check if equipment already exists
        if mongo.db.equipments.count_documents({}) == 0:
            equipment_data = [
                {'name': 'Microscope', 'description': 'High-resolution optical microscope for biological samples', 'available': True},
                {'name': 'Centrifuge', 'description': 'Laboratory centrifuge for separating substances', 'available': True},
                {'name': 'Spectrophotometer', 'description': 'Device for measuring light absorption', 'available': True},
                {'name': 'PCR Machine', 'description': 'Polymerase chain reaction thermal cycler', 'available': True},
                {'name': 'Incubator', 'description': 'Temperature-controlled chamber for cell culture', 'available': True}
            ]

            mongo.db.equipments.insert_many(equipment_data)
            print("Sample equipment data populated successfully!")
        else:
            print("Equipment data already exists.")

if __name__ == '__main__':
    populate_equipment()

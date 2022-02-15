import hashlib


class IDCreator:
    @staticmethod
    def create_id_for_allisons_visits(row_id, start):
        uuid = row_id + str(start)
        uuid = uuid.encode('utf-8')
        print(uuid)
        return hashlib.sha256(uuid).hexdigest()

import csv


class CsvInterface:
    def __init__(self, export_path):
        self.export_csv = export_path
        self.raw_data = None

    def CsvExport(self, raw_data=None):
        with open(self.export_csv, "a", encoding="utf-8") as csv_file:
            csv_writer = csv.writer(csv_file, quotechar=",", lineterminator='\n')
            csv_writer.writerows(raw_data)

    def CsvLineExport(self, raw_data=None):
        with open(self.export_csv, "a", encoding="utf-8") as csv_file:
            csv_writer = csv.writer(csv_file, quotechar=",", lineterminator='\n')
            csv_writer.writerows(raw_data)

from FlaskWebProject2.DAO.GetCandidates import getCandidates
from FlaskWebProject2.ViewModels.Candidates import Candidates
from FlaskWebProject2.Models.Candidate import Candidate

class CandidatesMB(object):
    """description of class"""
    def getCandidatesModel(self):
        candidates = Candidates()
        result = getCandidates()
        for row in result:
            candidates.add_candidate(Candidate(row['candidate_id'],row['Firstname'],row['Lastname'],row['EmailID'],row['Contact_Number'],row['Visa_Status'],row['College_Name1'],row['College_Name2'],row['Technology'],row['StartDate'],row['EndDate'],row['Vendor_Name'],row['Client_Name'],row['Job_Location'],row['dollarRate_per_hour']))
        return candidates
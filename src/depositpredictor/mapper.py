from depositpredictor.model import ContactType, DepositFeatures, JobType, MaritalStatus
from depositpredictor.predictor import InputData


class ModelInputFeaturesMapper:
    """Provides method to convert BL layer models to input features for ML models."""

    @staticmethod
    def to_input_features(df: DepositFeatures) -> InputData:
        return {
            "age": df.age,
            "education": df.education,
            "default": df.default,
            "balance": df.balance,
            "housing": df.housing,
            "loan": df.loan,
            "duration": df.duration,
            "campaign": df.campaign,
            "pdays": df.campaign if df.campaign else -1,
            "previous": df.previous,
            "job_blue_collar": df.job == JobType.BLUE_COLLAR,
            "job_entrepreneur": df.job == JobType.ENTREPRENEUR,
            "job_housemaid": df.job == JobType.HOUSEMAID,
            "job_management": df.job == JobType.MANAGEMENT,
            "job_retired": df.job == JobType.RETIRED,
            "job_self_employed": df.job == JobType.SELF_EMPLOYED,
            "job_services": df.job == JobType.SERVICES,
            "job_student": df.job == JobType.STUDENT,
            "job_technician": df.job == JobType.TECHNICIAN,
            "job_unemployed": df.job == JobType.UNEMPLOYED,
            "job_unknown": df.job == JobType.UNKNOWN,
            "marital_married": df.married == MaritalStatus.MARRIED,
            "marital_single": df.married == MaritalStatus.SINGLE,
            "contact_telephone": df.contact == ContactType.TELEPHONE,
            "contact_unknown": df.contact == ContactType.UNKOWN,
        }

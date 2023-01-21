from enum import StrEnum, auto, unique
from typing import Optional


@unique
class Classes(StrEnum):
    @classmethod
    def get(cls, val: str) -> Optional["Classes"]:
        val = val.strip()
        try:
            return cls(val)
        except ValueError:
            try:
                return cls[val]
            except KeyError:
                pass

    # Title
    TITLE_IC = auto()
    TITLE_MANAGER = auto()
    TITLE_EXECUTIVE = auto()

    # Company Category
    COMPANY_RPA = auto()
    COMPANY_CUSTOMER = auto()
    COMPANY_CONSULTANCY = auto()

    # Department
    DEPARTMENT_SALES = auto()
    DEPARTMENT_FINANCE = auto()
    DEPARTMENT_HR = auto()
    DEPARTMENT_IT = auto()
    DEPARTMENT_MARKETING = auto()
    DEPARTMENT_ENGINEERING = auto()
    DEPARTMENT_DATA_SCIENCE = auto()
    DEPARTMENT_LEGAL = auto()
    DEPARTMENT_MEDICAL = auto()
    DEPARTMENT_OPERATIONS = auto()
    DEPARTMENT_C_SUITE = auto()
    DEPARTMENT_RPA_COE = auto()
    DEPARTMENT_CUSTOMER_SUCCESS = auto()
    DEPARTMENT_RPA_DEVELOPMENT = auto()

    # Industry
    INDUSTRY_AGRICULTURE = auto()
    INDUSTRY_BUSINESS_SERVICES = auto()
    INDUSTRY_CONSTRUCTION = auto()
    INDUSTRY_CONSUMER_SERVICES = auto()
    INDUSTRY_EDUCATION = auto()
    INDUSTRY_ENERGY_UTILITIES_WASTE = auto()
    INDUSTRY_FINANCE = auto()
    INDUSTRY_GOVERNMENT = auto()
    INDUSTRY_HEALTHCARE_SERVICES = auto()
    INDUSTRY_HOLDING_COMPANIES_CONGLOMERATES = auto()
    INDUSTRY_HOSPITALITY = auto()
    INDUSTRY_HOSPITALS_PHYSICIANS_CLINICS = auto()
    INDUSTRY_INSURANCE = auto()
    INDUSTRY_LAW_FIRMS_LEGAL_SERVICES = auto()
    INDUSTRY_MANUFACTURING = auto()
    INDUSTRY_MEDIA_INTERNET = auto()
    INDUSTRY_MINERALS_MINING = auto()
    INDUSTRY_ORGANIZATIONS = auto()
    INDUSTRY_REAL_ESTATE = auto()
    INDUSTRY_RETAIL = auto()
    INDUSTRY_SOFTWARE = auto()
    INDUSTRY_TELECOMMUNICATIONS = auto()
    INDUSTRY_TRANSPORTATION = auto()
    INDUSTRY_RPA_SOFTWARE = auto()

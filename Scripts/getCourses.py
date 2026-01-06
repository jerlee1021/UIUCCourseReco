"""
Fetches course catalog data from the UIUC Course Explorer API.

Builds a path from optional components (year, semester, subject, course, CRN)
and requests the corresponding XML resource, saving the raw response to disk.

Examples:
- py getCourses.py
- py getCourses.py --year 2025 --semester fall
- py getCourses.py --year 2025 --semester fall --subject_code CS
- py getCourses.py --year 2025 --semester fall --subject_code CS --course_number 101
- py getCourses.py --year 2025 --semester fall --subject_code CS --course_number 101 --crn 12345
"""

import argparse
from typing import Optional
import requests
import sys
import xml.etree.ElementTree as ET

# Base API endpoint; path components are appended before the .xml suffix.
base_url = "http://courses.illinois.edu/cisapp/explorer/schedule/"

def get_course_info(
    year: Optional[str],
    semester: Optional[str],
    subject_code: Optional[str],
    course_number: Optional[str],
    crn: Optional[str],
) -> str:
    """
    Construct the API URL from optional components and return the raw XML text.

    The path hierarchy is:
    /schedule/{year}/{semester}/{subject_code}/{course_number}/{crn}.xml

    All parameters are optional; only provided components are appended in order.
    Note: If no components are given, this currently generates '/schedule/.xml',
    which is invalid. Consider special-casing to request '/schedule.xml'.
    """
    parts = []

    # Append year if provided
    if year is not None:
        parts.append(year)
    
    # Normalize semester to lowercase (API expects 'fall', 'spring', 'summer')
    if semester is not None:
        semester = semester.lower()
        parts.append(semester)

    # Normalize subject code to uppercase (e.g., 'CS', 'MATH')
    if subject_code is not None:
        subject_code = subject_code.upper()
        parts.append(subject_code)
    
    # Append course number (e.g., '101')
    if course_number is not None:
        parts.append(course_number)

    # Append CRN (e.g., '12345')
    if crn is not None:
        parts.append(crn)
    
    # Build final URL: join provided parts and add .xml suffix
    path = "/".join(parts) + ".xml"
    url = base_url + path

    # Perform request; return raw text for saving/inspection
    responses = requests.get(url)
    if responses.status_code != 200:
        return f"Error: Unable to fetch data for CRN {crn}. Status code: {responses.status_code}"
    return responses.text

def main():
    """
    Parse optional CLI arguments, fetch the XML, and save it to response.xml.

    All arguments are optional; the API path will include only those provided.
    """
    parser = argparse.ArgumentParser(description="Fetch course information from the university course catalog.")
    parser.add_argument("--year", type=str, default=None, help="Academic year (e.g., 2023)")
    parser.add_argument("--semester", type=str, default=None, help="Semester (fall, spring, summer)")
    parser.add_argument("--subject_code", type=str, default=None, help="Subject code (e.g., CS)")
    parser.add_argument("--course_number", type=str, default=None, help="Course number (e.g., 101)")
    parser.add_argument("--crn", type=str, default=None, help="Course registration number (CRN)")
    args = parser.parse_args()

    try:
        # Request XML content based on provided args
        xml_text = get_course_info(args.year, args.semester, args.subject_code, args.course_number, args.crn)
    except requests.HTTPError as e:
        # Handle HTTP errors explicitly (e.g., 4xx/5xx)
        print(f"HTTP error: {e}", file=sys.stderr)
        sys.exit(1)
    except requests.RequestException as e:
        # Handle connection/timeouts and other request-level issues
        print(f"Request failed: {e}", file=sys.stderr)
        sys.exit(1)

    # Persist the raw response for inspection or later parsing
    with open("response.xml", "wb") as f:
        f.write(xml_text.encode('utf-8'))

    print("\nSaved raw response to response.xml")

if __name__ == "__main__":
    main()
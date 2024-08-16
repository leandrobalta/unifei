import requests
import pymysql

# Configurações do banco de dados
db_config = {
    "host": "localhost",
    "user": "unifei",
    "password": "unifei",
    "db": "linkedin"
}

# Endereços da API fictícia (substitua por seus verdadeiros endpoints)
api_urls = {
    "personal": "http://api.exemplo.com/personal",
    "company": "http://api.exemplo.com/company",
    "job": "https://fresh-linkedin-profile-data.p.rapidapi.com/search-jobs?geo_code=106057199&date_posted=any_time&function_id=it,sale&industry_code=4,5&sort_by=most_relevant&start=0&easy_apply=false&under_10_applicants=false",
    "personal_company": "http://api.exemplo.com/personal_company"
}

def fetch_data(url):
    """Busca dados de uma API."""
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def insert_data(connection, query, data):
    """Insere dados no banco."""
    with connection.cursor() as cursor:
        cursor.execute(query, data)
    connection.commit()

def main():
    # Conectar ao banco de dados
    connection = pymysql.connect(**db_config)

    try:
        querystring = {"geo_code":"106057199","date_posted":"any_time","function_id":"it,sale","industry_code":"4,5","sort_by":"most_relevant","start":"0","easy_apply":"false","under_10_applicants":"false"}

        headers = {
            "X-RapidAPI-Key": "6759bfe495msh0c76b7499685515p19e07bjsnc283a1798d0d",
            "X-RapidAPI-Host": "fresh-linkedin-profile-data.p.rapidapi.com"
        }

        response = requests.get(api_urls["job"], headers=headers)
        
        if response:
            job_query = """
            INSERT INTO Job (job_id, job_title, job_description, job_url, location, posted_time, remote, salary, experience_level, company_id)
            VALUES (%(job_id)s, %(job_title)s, %(job_description)s, %(job_url)s, %(location)s, %(posted_time)s, %(remote)s, %(salary)s, %(experience_level)s, %(company_id)s)
            """
            
            resp = response.json()
            print(resp)
            # with connection.cursor() as cursor:
            #     cursor.execute(job_query, (resp.get("job_id"), resp.get("job_title"), resp.get("job_description"), resp.get("job_url"), resp.get("location"), resp.get("posted_time"), resp.get("remote"), resp.get("salary"), resp.get("experience_level"), resp.get("company_id")))
        
        # # Buscar e inserir dados de Personal
        # personal_data = fetch_data(api_urls['personal'])
        # if personal_data:
        #     personal_query = """
        #     INSERT INTO Personal (profile_id, first_name, last_name, full_name, headline, about, city, country, state, phone, email, linkedin_url, languages, job_title, school)
        #     VALUES (%(profile_id)s, %(first_name)s, %(last_name)s, %(full_name)s, %(headline)s, %(about)s, %(city)s, %(country)s, %(state)s, %(phone)s, %(email)s, %(linkedin_url)s, %(languages)s, %(job_title)s, %(school)s)
        #     """
        #     insert_data(connection, personal_query, personal_data)

        # # Buscar e inserir dados de Company
        # company_data = fetch_data(api_urls['company'])
        # if company_data:
        #     company_query = """
        #     INSERT INTO Company (company_id, company_name, employee_count, employee_range, hq_city, hq_country, hq_region, industries, linkedin_url, specialties, type, website)
        #     VALUES (%(company_id)s, %(company_name)s, %(employee_count)s, %(employee_range)s, %(hq_city)s, %(hq_country)s, %(hq_region)s, %(industries)s, %(linkedin_url)s, %(specialties)s, %(type)s, %(website)s)
        #     """
        #     insert_data(connection, company_query, company_data)

        # # Buscar e inserir dados de Job
        # job_data = fetch_data(api_urls['job'])
        # if job_data:
        #     job_query = """
        #     INSERT INTO Job (job_id, job_title, job_description, job_url, location, posted_time, remote, salary, experience_level, company_id)
        #     VALUES (%(job_id)s, %(job_title)s, %(job_description)s, %(job_url)s, %(location)s, %(posted_time)s, %(remote)s, %(salary)s, %(experience_level)s, %(company_id)s)
        #     """
        #     insert_data(connection, job_query, job_data)

        # # Buscar e inserir dados de Personal_Company
        # personal_company_data = fetch_data(api_urls['personal_company'])
        # if personal_company_data:
        #     personal_company_query = """
        #     INSERT INTO Personal_Company (profile_id, company_id, title, description, start_month, start_year, end_month, end_year, is_current, location)
        #     VALUES (%(profile_id)s, %(company_id)s, %(title)s, %(description)s, %(start_month)s, %(start_year)s, %(end_month)s, %(end_year)s, %(is_current)s, %(location)s)
        #     """
        #     insert_data(connection, personal_company_query, personal_company_data)

    finally:
        connection.close()



if __name__ == "__main__":
    main()

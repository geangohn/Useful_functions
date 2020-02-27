SELECT pid, state, age(backend_start, clock_timestamp()) as backend_start, age(xact_start, clock_timestamp()) as xact_start, age(query_start, clock_timestamp()) as query_start, age(state_change, clock_timestamp()) as state_change, usename, application_name, query
FROM pg_stat_activity
WHERE query NOT ILIKE '%pg_stat_activity%' AND usename = 'ivanmaksimov'
ORDER BY xact_start ASC, backend_start DESC;

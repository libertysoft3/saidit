#!/bin/bash

# exit immediately if a command exits with a non-zero status
set -e

# from setup_postgres.sh, can't run until 2 containers are running
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
create or replace function hot(ups integer, downs integer, date timestamp with time zone) returns numeric as \$\$
    select round(cast(log(greatest(abs((\$1 * 2) + \$2), 1)) * sign((\$1 * 2) + \$2) + (date_part('epoch', \$3) - 1134028003) / 45000.0 as numeric), 7)
\$\$ language sql immutable;

create or replace function upvotes(ups integer) returns integer as \$\$
    select \$1
\$\$ language sql immutable;

create or replace function score(ups integer, downs integer) returns integer as \$\$
    select (\$1 * 2) + \$2
\$\$ language sql immutable;

create or replace function controversy(ups integer, downs integer) returns float as \$\$
    select CASE WHEN \$1 < 0 or \$2 <= 0 THEN 0
                ELSE \$2 + (cast(\$1 as float) / (\$1 + \$2))
           END;
\$\$ language sql immutable;

create or replace function ip_network(ip text) returns text as \$\$
    select substring(\$1 from E'[\\d]+\.[\\d]+\.[\\d]+')
\$\$ language sql immutable;

create or replace function base_url(url text) returns text as \$\$
    select substring(\$1 from E'(?i)(?:.+?://)?(?:www[\\d]*\\.)?([^#]*[^#/])/?')
\$\$ language sql immutable;

create or replace function domain(url text) returns text as \$\$
    select substring(\$1 from E'(?i)(?:.+?://)?(?:www[\\d]*\\.)?([^#/]*)/?')
\$\$ language sql immutable;

EOSQL

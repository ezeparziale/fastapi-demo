-- SEQUENCE: public.posts_id_seq

-- DROP SEQUENCE IF EXISTS public.posts_id_seq;

CREATE SEQUENCE IF NOT EXISTS public.posts_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 9223372036854775807
    CACHE 1;

ALTER SEQUENCE public.posts_id_seq
    OWNER TO fastapi;

-- Table: public.posts

-- DROP TABLE IF EXISTS public.posts;

USE fastapi

CREATE TABLE IF NOT EXISTS public.posts
(
    id integer NOT NULL DEFAULT nextval('posts_id_seq'::regclass),
    title character varying COLLATE pg_catalog."default" NOT NULL,
    content character varying COLLATE pg_catalog."default" NOT NULL,
    published boolean NOT NULL DEFAULT true,
    created_at timestamp without time zone NOT NULL DEFAULT now(),
    CONSTRAINT posts_pkey PRIMARY KEY (id)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.posts
    OWNER to fastapi;
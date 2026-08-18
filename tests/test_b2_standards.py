from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ENV_SAMPLE_FILES = (".env.example", ".env.template")
STANDARD_B2_KEYS = {
    "B2_APPLICATION_KEY_ID",
    "B2_APPLICATION_KEY",
    "B2_BUCKET_NAME",
    "B2_REGION",
    "B2_PUBLIC_URL_BASE",
}
LEGACY_ENV_ALIASES = {
    "AWS_ACCESS_KEY_ID",
    "AWS_SECRET_ACCESS_KEY",
    "B2_ENDPOINT",
    "B2_KEY_ID",
    "B2_S3_ENDPOINT",
}
NATIVE_B2_MARKERS = {
    "b2-native",
    "b2_upload_file",
    "b2_get_upload_url",
    "b2_authorize_account",
}


def _env_keys(path: Path) -> set[str]:
    keys = set()
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        keys.add(line.split("=", 1)[0])
    return keys


def test_env_sample_files_stay_in_sync():
    canonical = (ROOT / ".env.example").read_text(encoding="utf-8")
    alias = (ROOT / ".env.template").read_text(encoding="utf-8")

    assert alias == canonical


def test_env_examples_use_standard_b2_names():
    for name in ENV_SAMPLE_FILES:
        keys = _env_keys(ROOT / name)

        assert STANDARD_B2_KEYS <= keys
        assert keys.isdisjoint(LEGACY_ENV_ALIASES)


def test_no_native_b2_api_markers():
    searchable = [
        ROOT / "README.md",
        ROOT / "agent_demo.ipynb",
        ROOT / "agent_demo_deepseek.ipynb",
    ]

    for path in searchable:
        text = path.read_text(encoding="utf-8")
        found = {marker for marker in NATIVE_B2_MARKERS if marker in text}
        assert not found, f"{path.name} contains native B2 API markers: {found}"


def test_s3_client_guidance_mentions_required_user_agent():
    readme = (ROOT / "README.md").read_text(encoding="utf-8")

    assert "S3-compatible API" in readme
    assert "(backblaze-b2-samples)" in readme

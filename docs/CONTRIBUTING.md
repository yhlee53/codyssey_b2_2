# Contributing Guide

## 브랜치 전략 (GitHub Flow)
- `main` — 항상 배포 가능한 상태
- `*`    — 작업 단위 브랜치 (bal, son, thin, yrei, yhlee)

우리 팀이 GitHub Flow를 선택한 이유(3줄 이내): 

## 브랜치 네이밍 규칙
- 예: `<topic>`

## 커밋 메시지 컨벤션
- 형식 예: `feat: subject`, `fix: subject`, `docs: subject`, `refactor: subject`
- 금지 예: `update`, `wip`, `temp` 등

## PR 규칙
- PR 본문 필수 항목: 변경 사항(What), 변경 이유(Why), 테스트/검증(How)
- PR 본문에 `Closes #<issue_number>` 또는 `Fixes #<issue_number>` 포함
- 병합 조건: 최소 1명 승인, CI 통과(있으면)

## 코드 리뷰 규칙
- 단순 "LGTM"만 허용하지 않음: 실질 코멘트 1개 이상 필요
- 리뷰어/작성자 간 최소 1회 상호작용 필요

## 충돌 대응 흐름
- 충돌 발생 → 관련자 알림 → 로컬/브랜치에서 해결 → 결과 문서화(docs/conflict-resolution.md)

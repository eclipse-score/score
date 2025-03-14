#!/bin/bash
set -eu

# All the commands we want to try
COMMANDS=(
  "bazel run //docs:ide_support"
  "bazel run //docs2:ide_support"
  "bazel run //docs:incremental"
  "bazel run //docs2:incremental"
  "bazel build //docs:incremental && bazel-bin/docs/incremental"
  "bazel build //docs2:incremental && bazel-bin/docs2/incremental"
  "bazel build //docs:docs"
  "bazel build //docs2:docs"
  "bazel run //docs:live_preview"
  "bazel run //docs2:live_preview"
  "bazel build //docs:live_preview && bazel-bin/docs/live_preview"
  "bazel build //docs2:live_preview && bazel-bin/docs2/live_preview"
)

# Array to store results
declare -A RESULTS

# Run all the commands, print out the command and the result, and store results
for cmd in "${COMMANDS[@]}"; do
  echo "Running command: $cmd"
  if bash -c "$cmd"; then
    echo "Command succeeded"
    RESULTS["$cmd"]="✅"
  else
    echo "Command failed"
    RESULTS["$cmd"]="❌"
  fi
done

# Print Markdown table summary
echo -e "\n### Summary\n"
echo "| Command | Result |"
echo "|---------|--------|"
for cmd in "${COMMANDS[@]}"; do
  echo "| \`$cmd\` | ${RESULTS[$cmd]} |"
done

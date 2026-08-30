"""Task-specific paired-item plans, mechanical advice and transparent scoring."""
import random
import re


def validate_subject_id(value):
    if isinstance(value, bool) or not re.fullmatch(r'[1-9][0-9]{2}', str(value)):
        raise ValueError('subject_id must be an integer from101to999')
    number = int(value)
    if number < 101:
        raise ValueError('subject_id must be an integer from101to999')
    return number


def make_plans(n_trials, labels, item_ids, offsets, seed):
    """BlockUnit generator: no repeated items, balanced distance×direction cells."""
    if n_trials != len(item_ids) or n_trials % len(labels):
        raise ValueError('Item count must equal n_trials and balance all six cells')
    if len(set(item_ids)) != len(item_ids):
        raise ValueError('Items cannot repeat within a participant')
    rng = random.Random(int(seed))
    items = list(item_ids)
    cells = list(labels) * (n_trials // len(labels))
    rng.shuffle(items)
    rng.shuffle(cells)
    return [f'{item}|{cell}|{rng.choice(offsets[cell.rsplit("_",1)[0]])}'
            for item, cell in zip(items, cells)]


def decode_plan(plan):
    item_id, cell, offset = plan.split('|')
    distance, direction = cell.rsplit('_', 1)
    return item_id, cell, distance, direction, int(offset)


def parse_integer(raw, limit):
    text = str(raw).strip()
    if not text:
        return None, 'blank'
    if not re.fullmatch(r'[+-]?[0-9]+', text):
        return None, 'invalid_format'
    # Bound length before int conversion, including hostile extremely long entry.
    significant = text.lstrip('+-').lstrip('0')
    if len(significant) > 10:
        return None, 'out_of_range'
    value = int(text) if len(text) < 4000 else int(('-' if text.startswith('-') else '') + (significant or '0'))
    if abs(value) > limit:
        return None, 'out_of_range'
    return value, 'valid'


def entry_outcome(raw, submitted, rt, limit, plausible_min, plausible_max):
    value, status = parse_integer(raw, limit)
    return dict(raw_text=str(raw), submitted=bool(submitted), rt=rt,
                draft_value=value, value=value if submitted and status == 'valid' else None,
                valid=bool(submitted and status == 'valid'), status=status if submitted else 'timeout',
                plausible_year=(plausible_min <= value <= plausible_max) if submitted and status == 'valid' else None)


def make_advice(initial, truth, direction, offset, limit):
    result = dict(advice_value=None, advice_status='initial_unavailable', requested_offset=offset,
                  requested_direction=direction, actual_delta=None, initial_equals_truth=None,
                  realized_direction=None, advice_absolute_error=None, advice_accuracy_gain=None)
    if initial is None:
        return result
    tie = initial == truth
    toward_sign = 1 if initial <= truth else -1
    sign = toward_sign if direction == 'toward' else -toward_sign
    delta = sign * offset
    advice = initial + delta
    result.update(initial_equals_truth=tie, actual_delta=delta,
                  realized_direction='from_truth_tie' if tie else direction)
    if abs(advice) > limit:
        result['advice_status'] = 'advice_out_of_range'
        return result
    result.update(advice_value=advice, advice_status='available',
                  advice_absolute_error=abs(advice-truth),
                  advice_accuracy_gain=abs(initial-truth)-abs(advice-truth))
    return result


def score_pair(initial, advice, final, truth):
    result = dict(signed_revision=None, absolute_revision=None, signed_advice_distance=None,
                  absolute_advice_distance=None, weight_of_advice=None, absolute_revision_ratio=None,
                  self_weight=None, weight_status='missing_value', primary_eligible=False,
                  initial_absolute_error=abs(initial-truth) if initial is not None else None,
                  final_absolute_error=abs(final-truth) if final is not None else None,
                  accuracy_gain=None)
    if initial is not None and advice is not None:
        result.update(signed_advice_distance=advice-initial, absolute_advice_distance=abs(advice-initial))
    if initial is not None and final is not None:
        result.update(signed_revision=final-initial, absolute_revision=abs(final-initial),
                      accuracy_gain=abs(initial-truth)-abs(final-truth))
    if initial is None or advice is None or final is None:
        return result
    denominator = advice-initial
    if denominator == 0:
        result['weight_status'] = 'zero_advice_distance'
        return result
    weight = (final-initial)/denominator
    result.update(weight_of_advice=weight, self_weight=1-weight,
                  absolute_revision_ratio=abs(final-initial)/abs(denominator),
                  weight_status='defined', primary_eligible=True)
    return result
